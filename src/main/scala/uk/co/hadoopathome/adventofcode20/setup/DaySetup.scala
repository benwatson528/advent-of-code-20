package uk.co.hadoopathome.adventofcode20.setup

import scala.io.Source
import scala.sys.process.Process
import scala.util.Using

object DaySetup extends App {
  println("Please enter a day to be setup:")
  val day = scala.io.StdIn.readInt().toString
  val puzzleUrl = "https://adventofcode.com/2020/day/" + day
  val puzzleName = getPuzzleName(puzzleUrl)

  val scriptPath = "src/main/resources/script/create-day.sh"
  val scriptRunCommand = Set("bash", scriptPath, day, puzzleName).mkString(" ")
  println(s"Running day creation command: $scriptRunCommand")
  val process = Process(scriptRunCommand).run()
  println(s"Setup script exit value = ${process.exitValue()}")

  private def getPuzzleName(puzzleUrl: String): String = {
    val entirePage = Using(Source.fromURL(puzzleUrl)) { source => source.mkString }.get
    val puzzleName = entirePage.split("--- ")(1).split(" ---")(0).split(": ")(1)
    val trimmedPuzzleName = puzzleName.split(" ").map(_.capitalize).mkString

    //Scala class names can't start with numbers
    if (trimmedPuzzleName.head.isDigit) {
      "A" + trimmedPuzzleName
    } else {
      trimmedPuzzleName
    }
  }
}
