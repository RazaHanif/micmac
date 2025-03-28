import { Text, View, Image, StyleSheet, Appearance, Platform, FlatList, ScrollView, Pressable} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Link } from "expo-router";
import "./global.css"
import { data } from '@/data/todo'

const Index = () => {
  const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  const styles = createStyles()

  return (
    <Container>
      <FlatList
        data={ data }
        keyExtractor={ (item) => item.id.toString() }
        showsVerticalScrollIndicator={ false }
        contentContainerStyle={ styles.content }
        ListEmptyComponent={
          <Text style={ styles.empty }>
            No Tasks!
          </Text>
        }
        renderItem={ ({ item }) => (
          <View style={styles.card}>
            <View style={styles.task}>
              <Text style={
                [
                  styles.text,
                  item.completed ? styles.completed : null
                ]
              }>
                { item.title }
              </Text>
            </View>
            <View style={styles.delete}>
              <Link 
                href="/menu" 
                style={{ marginHorizontal: 'auto' }} 
                asChild
              >
                <Pressable style={styles.btn}>
                  <Text style={styles.btnText}>
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

function createStyles() {
  return StyleSheet.create({
      content: {
        bg
          
      },
    })
  }

export default Index