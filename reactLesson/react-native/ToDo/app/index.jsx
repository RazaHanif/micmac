import { Text, View, Platform, FlatList, ScrollView, Pressable} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Link } from "expo-router";
import "./global.css"
import { data } from '@/data/todo'
import 'nativewind'

const Index = () => {
  const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  const styles = {
    content: "flex-1 p-4 bg-primary",
    empty: "text-center text-gray-500 text-lg",
    card: "bg-white p-4 rounded-lg shadow mb-2 flex-row justify-between",
    task: "flex-1",
    text: "text-lg text-text",
    completed: "line-through text-textDim",
    delete: "flex-shrink-0",
    btnLink: "mx-auto",
    btn: "bg-red-500 px-4 py-2 rounded",
    btnText: "text-white font-bold",
  }

  return (
    <Container className={"flex-1 p-4 bg-primary"}>
      <FlatList
        data={ data }
        keyExtractor={ (item) => item.id.toString() }
        showsVerticalScrollIndicator={ false }
        ListEmptyComponent={
          <Text className={ styles.empty }>
            No Tasks!
          </Text>
        }
        renderItem={ ({ item }) => (
          <View className={styles.card}>
            <View className={styles.task}>
              <Text className={
                `
                 ${styles.text} 
                 ${item.completed ? styles.completed : ''}
                `
              }>
                { item.title }
              </Text>
            </View>
            <View className={styles.delete}>
              <Link 
                href="/menu" 
                className={styles.btnLink} 
                asChild
              >
                <Pressable className={styles.btn}>
                  <Text className={styles.btnText}>
                    X
                  </Text>
                </Pressable>
              </Link>
            </View>
          </View>
        )}
      />
    </Container>
  );
}

export default Index