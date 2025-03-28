import { View, Text, StyleSheet } from 'react-native'
import React from 'react'

const about = () => {
  return (
    <View style={styles.bg}>
      <Text style={styles.textsmall}>
        Relaxed local-chain venue serving atrisanal coffies, baked products & sweet treats.
      </Text>
      <Text style={styles.text}>
        Location: 10499 Islington Ave, Kleinburg, ON
      </Text>
      <Text style={styles.text}>
        Phone: (905) 552-0155
      </Text>
      <Text style={styles.text}>
        Hours: 7:30am - 6:00pm        
      </Text>
    </View>
  )
}

export default about

const styles = StyleSheet.create({
  bg: {
    display: 'flex',
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#123123',
  },
  text: {
    color: 'white',
    width: '100%',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
    padding: 20,
  },
  textsmall: {
    color: 'white',
    width: '100%',
    fontSize: 14,
    textAlign: 'center',
    marginVertical: 20,
  }
})