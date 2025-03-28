import { Text, View, Platform, FlatList, ScrollView, Pressable} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Link } from "expo-router";
import "./globals.css";
import { data } from '@/data/todo';

const Index = () => {
  const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  const deleteTask = (itemId) => {
    console.log(itemId)
  }

  return (
    <Container className={"flex-1 p-4 bg-primary"}>
      <View>
        <Text>Add a Task</Text>
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