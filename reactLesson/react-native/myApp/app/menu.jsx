import { View, Text, Image, StyleSheet, Appearance, Platform, SafeAreaView, FlatList } from 'react-native'
import { ScrollView } from 'react-native-gesture-handler'
import { Colors } from '@/constants/Colors'
import { MENU_ITEMS } from '@/constants/MenuItems'
import MENU_IMAGES from '@/constants/MenuImages'

const MenuScreen = () => {
    const colorScheme = Appearance.getColorScheme()

    const theme = colorScheme === 'dark' ? Colors.dark : Colors.light

    const styles = createStyles(theme, colorScheme)

    const Container = Platform.OS === 'web' ? ScrollView : SafeAreaView

    const separatorComp = <View style={styles.separator} />

    const footerComp = <Text style={styles.footer}>End of Menu</Text>

  return (
    <Container>
        <FlatList
            data={MENU_ITEMS}
            keyExtractor={(item) => item.id.toString()}
            showsVerticalScrollIndicator={false}
            contentContainerStyle={styles.content}
            ItemSeparatorComponent={separatorComp}
            ListFooterComponent={footerComp}
            ListEmptyComponent={
                <Text style={styles.err}>
                    No items
                </Text>
            }
            renderItem={({ item }) => (
                <View style={styles.card}>
                    <View style={styles.text}>
                        <Text style={styles.title}>
                            { item.title }
                        </Text>
                        <Text style={styles.desc}>
                            { item.description }
                        </Text>
                    </View>
                    <Image
                        source={MENU_IMAGES[item.id - 1]}
                        style={styles.img}
                    />
                </View>
            )}
        />
    </Container>
  )
}

function createStyles(theme, colorScheme) {
    return StyleSheet.create({
        content: {
            paddingTop: 10,
            paddingBottom: 20,
            paddingHorizontal: 12,
            backgroundColor: theme.background,
        },
        separator: {
            height: 1,
            backgroundColor: colorScheme === 'dark' ? 'papayawhip' : 'black',
            width: '50%',
            maxWidth: 300,
            marginHorizontal: 'auto',
            marginBottom: 10
        },
        card: {
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            margin: 10,
            padding: 10,
            backgroundColor: 'grey',
            borderRadius: 10
        },
        text: {
            paddingBottom: 20
        },
        title: {
            fontSize: 24,
            fontWeight: 'bold',
            textAlign: 'center'
        },
        err: {
            color: 'red',
            fontSize: 24,
            fontWeight: 'bold',
            textAlign: 'center'
        },
        desc: {
            fontSize: 14,
            textAlign: 'center'
        },
        img: {
            width: 150,
            height: 150,
            resizeMode: 'stretch'
        },
        footer: {
            color : colorScheme === 'dark' ? 'papayawhip' : 'black',
            marginHorizontal: 'auto',
        }
    })
}

export default MenuScreen