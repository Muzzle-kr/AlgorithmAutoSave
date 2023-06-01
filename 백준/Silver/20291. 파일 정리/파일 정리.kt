import java.util.*

fun main() {
    val extDict = HashMap<String, Int>()
    val scanner = Scanner(System.`in`)

    val n = scanner.nextInt()
    scanner.nextLine() // Consume the newline character after reading the integer

    for (i in 0 until n) {
        val input = scanner.nextLine()
        val (name, ext) = input.split(".")
        extDict[ext] = extDict.getOrDefault(ext, 0) + 1
    }

    val sortedResult = extDict.entries.sortedBy { it.key }

    for ((name, ext) in sortedResult) {
        println("$name $ext")
    }
}