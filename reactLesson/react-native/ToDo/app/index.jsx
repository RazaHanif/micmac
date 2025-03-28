import { Text, View, Platform, FlatList, ScrollView, Pressable} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Link } from "expo-router";
import "./globals.css";
import { data } from '@/data/todo';
import { useState } from "react";

const Index = () => {
  const [tasks, setTasks] = useState(data)

  const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  const addTask = (newTask) => {
    const length = tasks.length()

    const task = {
      "id": length + 1,
      "title": newTask,
      "completed": false
    }

    setTasks([...tasks, task])
  }

  const deleteTask = (itemId) => {
    let task = tasks[itemId - 1]
  
    task.completed = true

    setTasks([...tasks, task])
  }

  return (
    <Container className={"flex-1 p-4 bg-primary"}>
      <View className="">
        

      </View>

      <FlatList
        data={ data }
        keyExtractor={ (item) => item.id.toString() }
        showsVerticalScrollIndicator={ false }
        ListEmptyComponent={
          <Text className={"text-center text-error text-lg"}>
            No Tasks!
          </Text>
        }
        renderItem={ ({ item }) => (
          <View className={"bg-white p-4 rounded-lg shadow mb-2 flex-row justify-between"}>
            <View className={"flex-1"}>
              <Text className={
                ` text-lg text-text
                 ${item.completed ? 'line-through text-textDim' : ''}
                `
              }>
                { item.title }
              </Text>
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