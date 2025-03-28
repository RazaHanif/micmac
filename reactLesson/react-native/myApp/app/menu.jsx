import { View, Text, StyleSheet, Appearance, Platform, SafeAreaView, FlatList } from 'react-native'
import { Colors } from '@/constants/Colors'
import { ScrollView } from 'react-native-gesture-handler'

const MenuScreen = () => {
    const colorScheme = Appearance.getColorScheme()

    const theme = colorScheme === 'dark' ? Colors.dark : Colors.light

    const styles = createStyles(theme, colorScheme)

    const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

  return (
    <Container>
        <FlatList
            data={[]}
            renderItem={({ item }) => {}}
        />
    </Container>
  )
}

function createStyles(theme, colorScheme) {
    return StyleSheet.create({

    })
}

export default MenuScreen