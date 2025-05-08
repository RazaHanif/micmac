import { useLocalSearchParams } from "expo-router";
import { View, Text, StyleSheet, Pressable, TextInput } from "react-native"

import { useState, useEffect, useContext } from 'react'
import { SafeAreaView } from "react-native-safe-area-context";
import { useRouter } from "expo-router";

export default function EditScreen() {
    const { id } = useLocalSearchParams()
    const [todo, setTodo] = useState({})
    const router = useRouter()

    useEffect(() => {

    }, [])

    return (
        <View>
            <Text>{id}</Text>
        </View>
    )
}