package uk.co.hadoopathome.adventofcode20.${internal_day}

import org.scalatest.funsuite.AnyFunSuite

import scala.io.Source

class ${internal_class_name}Test extends AnyFunSuite {
  test("sumNumbers +1, +1, +1") {
    val input = List(1, 1, 1)
    assert(${internal_class_name}.sumNumbers(input) === 3)
  }

  test("sumNumbers real") {
    val input = Source.fromResource("${internal_day}/input.txt").getLines.toList
        .map(_.toString.toInt)
    assert(${internal_class_name}.sumNumbers(input) === 435)
  }
}
