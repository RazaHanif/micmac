import { View, Text, StyleSheet, ImageBackground, Pressable } from 'react-native'
import { Link } from 'expo-router'
import icedCoffeeImg from '@/assets/images/iced-coffee.png'


const app = () => {
  return (
    <View style={styles.container}>
      <ImageBackground 
        source={icedCoffeeImg}
        resizeMode='cover'
        style={styles.image}
      >
        <Text style={styles.text}>Balzac's Coffee Roasters</Text>

        {/* Button  */}
        <Link href="/menu" style={{ marginHorizontal: 'auto' }} asChild>
          <Pressable style={styles.btn}>
            <Text style={styles.btnText}>
              Menu
            </Text>
          </Pressable>
        </Link>
        <Link href="/contact" style={{ marginHorizontal: 'auto' }} asChild>
          <Pressable style={styles.btn}>
            <Text style={styles.btnText}>
              Contact
            </Text>
          </Pressable>
        </Link>
      </ImageBackground>
    </View>
  )
}

export default app

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  },
  image: {
    width: '100%',
    height: '100%',
    flex: 1,
    resizeMode: 'cover',
    justifyContent: 'center',
  },
  text: {
    color: 'white',
    fontSize: 42,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
    marginBottom: 120
  },
  link: {
    color: 'blue',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    textDecorationLine: 'underline',
    backgroundColor: 'rgba(0,0,0,0.5)',
    padding: 20
  },
  btnText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
    padding: 4,
  },
  btn: {
    height: 60,
    width: 150,
    borderRadius: 20,
    justifyContent: 'center',
    backgroundColor: 'rgba(0,0,0,0.75)',
    padding: 6,
    marginBottom: 50
  }
})