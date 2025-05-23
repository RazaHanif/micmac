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
                        <Text style={[styles.title, styles.desc]}>
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
            flexDirection: 'row',
            width:'100%',
            maxWidth: 600,
            height: 100,
            marginBottom: 10,
            borderStyle: 'solid',
            borderColor: colorScheme === 'dark' ? 'papayawhip' : 'black',
            borderWidth: 1,
            borderRadius: 20,
            overflow: 'hidden',
            marginHorizontal: 'auto',
            // backgroundColor: 'grey',
        },
        text: {
            width: '65%',
            paddingTop: 10,
            paddingLeft: 10,
            paddingRight: 5,
            flexGrow: 1
        },
        title: {
            fontSize: 18,
            textDecorationLine: 'underline',
            fontWeight: 'bold',
            textAlign: 'center'
        },
        err: {
            color: 'red',
            fontSize: 24,
            fontWeight: 'bold',
        },
        desc: {
            color: theme.text,
        },
        img: {
            width: 100,
            height: 100
        },
        footer: {
            color : colorScheme === 'dark' ? 'papayawhip' : 'black',
            marginHorizontal: 'auto',
        }
    })
}

export default MenuScreen