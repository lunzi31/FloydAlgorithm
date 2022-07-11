import unittest

class Vertices(unittest.TestCase):
    """Test for number of vertices"""
    def testvertices(self):
        vertices = [1,1,1,1]
        result = sum(vertices)
        self.assertEqual(result, 5)

class TestSolution(unittest.TestCase):
    """Test for correct answer for shortest route solution"""
    def testsolution01(self):
        """Testing solution on graph supplied"""
        graph = [[0,7,NoPath,8],
        [NoPath,0,5,NoPath],
        [NoPath,NoPath,0,2],
        [NoPath,NoPath,NoPath,0]]

        solution_distance = floyd(0, 0, 0, graph)
        known_distance = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]

        print("testsolution01distance:", solution_distance)
        self.assertEqual(known_distance, solution_distance)

    def testsolution02(self):
        """Testing solution on mal-input"""
        graph = [
            [0, 7, 'Twelve', 8],
            [NoPath, 0, 5, NoPath],
            [NoPath, NoPath, 0, 2],
            [NoPath, NoPath, NoPath, 0]
            ]
        solution_distance = floyd(0, 0, 0, graph)
        known_distance = [
            [0, 7, 12, 8],
            [9223372036854775807, 0, 5, 7],
            [9223372036854775807, 9223372036854775807, 0, 2],
            [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
            ]
        print("testsolution02distance:", solution_distance)
        self.assertEqual(known_distance, solution_distance)

if __name__ == '__main__':
    unittest.main()