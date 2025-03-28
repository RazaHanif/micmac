import { Text, View, Image, StyleSheet, Appearance, Platform, FlatList, ScrollView } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
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
                  
                ]
              }>
                { item.title }
              </Text>
            </View>
          </View>
        )}
      />
      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Text>Edit app/index.tsx to edit this screen.</Text>
      </View>
    </Container>
  );
}

function createStyles() {
  return StyleSheet.create({
      content: {
          
      },
    })
  }

export default Index