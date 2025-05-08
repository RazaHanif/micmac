import { Text, View, Platform, FlatList, ScrollView, Pressable, TextInput} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import "./globals.css";
import { data } from '@/data/todo';
import { useState } from "react";
import { useRouter } from "expo-router";

import { Inter_500Medium, useFonts } from "@expo-google-fonts/inter"

const Index = () => {
  const [tasks, setTasks] = useState([...data])
  const [inputText, setInputText] = useState("")
  const router = useRouter()

  const [loaded, error] = useFonts({
    Inter_500Medium
  })

  if (!loaded && !error) {
    return null
  }

  const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  const addTask = () => {
    if (inputText) {
      const length = tasks.length
      const task = {
        "id": length + 1,
        "title": inputText,
        "completed": false
      }
      setTasks((prevTasks) => [task, ...prevTasks])
      setInputText("")
    }
  }

  const deleteTask = (itemId) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === Number(itemId) ? { ...task, completed: true } : task
      )
    )
  }

  const handlepress = (itemId) => {
    router.push(`/todos/${itemId}`)
  }

  return (
    <Container className={"flex-1 p-4 bg-primary font-(Inter_500Medium)"}>
      <View className={"flex-row w-full justify-between align-middle"}>
        <TextInput
          className={"border-solid border border-text rounded-lg p-2 my-auto flex-grow text-secondary"}
          placeholder="Add a new todo"
          value={inputText}
          onChangeText={setInputText}
        />
        <Pressable
          className={"bg-good p-2 m-2 rounded-lg box-border border border-solid border-good"}
          onPress={addTask}
        >
          <Text className={"text-secondary font-bold text-center"}>Submit</Text>
        </Pressable>
      </View>

      <FlatList
        data={ tasks }
        keyExtractor={ (item) => item.id }
        showsVerticalScrollIndicator={ false }
        ListHeaderComponent={
          <View className="h-[1] bg-textDim w-[100%] rounded mx-auto my-2" />
        }
        ListFooterComponent={
          <View className="h-[1] bg-textDim w-[100%] rounded mx-auto my-2" />
        }
        ListEmptyComponent={
          <Text className={"text-center text-error text-lg"}>
            No Tasks!
          </Text>
        }
        ItemSeparatorComponent={
          <View className="h-1 bg-text w-[100%] rounded mx-auto mb-2" />
        }
        renderItem={ ({ item }) => (
          <View className={"p-2 rounded-lg shadow mb-2 flex-row justify-between"}>
            <View className={"flex-1"}>
              <Pressable
                onPress={ () => handlePress(item.id)}
              >
                <Text className={
                  ` text-lg
                  ${item.completed ? 'line-through text-textDim' : 'text-secondary'}
                  `
                }>
                  { item.title }
                </Text>
              </Pressable>
            </View>
            <View className={"flex-shrink-0"}>
              <Pressable className={"bg-red-500 px-4 py-2 rounded"} onPress={() => deleteTask(item.id)}>
                <Text className={"text-white font-bold"}>
                  X
                </Text>
              </Pressable>
            </View>
          </View>
        )}
      />
    </Container>
  );
}

export default Index