from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from markdown2 import Markdown
from . import util
import random
import re


# Default page, displays a list of links
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Goes to a specific entry, if an entry does not exist displays an error
def entry(request, title):
    content = util.get_entry(title)
    entry = title.capitalize() 
    
    # Error handling
    if not content:
        return render(request, "encyclopedia/error.html", {
        "error_type": "Not Found",
        "error_desc": f"{entry} page not found, does not exist"
        })
    
    # using markdowner to convert Markdown to HTML 
    markdowner = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "entries": [markdowner.convert(content),],
        "title": entry
    })


# Functionality for search in sidebar, with error handling 
# POST ONLY
def search(request):
    if request.method == "POST":
        content = util.get_entry(request.POST["q"])
        
        # Shows suggested answers
        if not content:
            suggested_entries = sugg_entries(request.POST["q"])
            return render(request, "encyclopedia/search.html", {
                "entries": suggested_entries,
                "query": request.POST["q"]
            }) 
        return HttpResponseRedirect(reverse("entry", args=(request.POST["q"],)))


# New entry handling, with error checking
# GET - shows default page
# POST - saves entry
def entry_new(request):
    if request.method == "POST":
        title = str(request.POST["title"])
        text = request.POST["text"]
        
        # Error handling
        if title.upper() in (item.upper() for item in util.list_entries()):
            return render(request, "encyclopedia/error.html", {
                "error_type": "Entry Already Exists",
                "error_desc": f"{title} page already exists",
                "error_redirect": title
            })
        # Saves file to disk
        write_file(title, text)        
        return HttpResponseRedirect(reverse("entry", args=(title,)))

        
    return render(request, "encyclopedia/add.html", {
        "entries": util.list_entries()
    })


# Existing entry handling, with error checking
# GET - shows default page with file info loaded into <textarea>
# POST - saves entry
def entry_edit(request, title):
    if request.method == "POST":
        title = str(request.POST["title"])
        text = str(request.POST["text"])    
        
        # Override saves file to disk 
        write_file(title, text, True)        
        return HttpResponseRedirect(reverse("entry", args=(title,)))
    
    if str(title) in util.list_entries():
        with open(f"entries/{title}.md", "r") as md_file:
            md_text = md_file.read()
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": md_text
                })
            
    # Error handling
    return render(request, "encyclopedia/error.html", {
        "error_desc": f"{title} Page Not Found"
        })

# Function to get random page load 
def entry_random(request):
    entries = util.list_entries()
    return HttpResponseRedirect(reverse("entry", args=(entries[random.randrange(len(entries))],)))
    
# Regex handling for search
def sugg_entries(query):
    search = re.compile(f".*{query}.*", re.IGNORECASE)
    return list(filter(search.match, util.list_entries()))


# Reusable function to handling saving user input
def write_file(title, content, edit=False):
    with open(f"entries/{title}.md", "w") as md_file:
            if not edit:
                md_file.write(f"# {title}\n\n")
            md_file.write(content)
