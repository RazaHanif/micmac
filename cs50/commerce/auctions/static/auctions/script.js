let full_desc
let more_btn
let text
let short_text
let textarea

window.onload = () => {
    full_desc = document.querySelector("#desc_full")
    more_btn = document.querySelector("#more")
    text = full_desc.innerHTML
    short_text = text.substring(0, 150)
    full_desc.innerHTML = `${short_text}...`

    textarea = document.querySelector("#id_comment")
    textarea.placeholder = "New Comment"
};

function show() {
    more_btn.style.visibility = "hidden"
    full_desc.innerHTML = text
}