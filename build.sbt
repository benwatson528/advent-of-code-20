name := "advent-of-code-20"

version := "0.1"

scalaVersion := "2.13.3"

libraryDependencies += "org.scalactic" %% "scalactic" % "3.2.2"
libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.2" % "test"

// Required to stop IntelliJ complaining about missing dependencies - see https://stackoverflow.com/a/58456468/729819
ThisBuild / useCoursier := false
