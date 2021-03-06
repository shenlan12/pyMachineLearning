# coding:utf-8
import math
import unittest
import sys
sys.path.append("../../")
from louvain.pylouvain import PyLouvain
from louvain.oldlouvain import PyLouvain as LouvainOld


class PylouvainTest(unittest.TestCase):
    def tearDown(self):
        print('***AFTER ONE TEST***')

    def setUp(self):
        print('***BEFORE ONE TEST***')

    @classmethod
    def tearDownClass(self):
         print('FINISHED...')

    @classmethod
    def setUpClass(self):
        print('STARTING...')
        
    def test_arxiv(self):
        pyl = PyLouvain.from_file("data/arxiv.txt")
        partition, finalPartit, q = pyl.apply_method()

    def test_citations(self):
        pyl = PyLouvain.from_file("data/hep-th-citations")
        partition, finalPartit, q = pyl.apply_method()

    def test_karate_club(self):
        pyl = PyLouvain.from_file("data/karate.txt")
        partition, finalPartit, q = pyl.apply_method(draw=True)
        q_ = q * 10000
        #self.assertEqual(4, len(partition))
        #self.assertEqual(4298, math.floor(q_))
        #self.assertEqual(4299, math.ceil(q_))
        print("Before trans PARTITON IS " , partition)
        print("FINAL PARTITON IS " , finalPartit)    

    def test_karate_club_old(self):
        pyl = LouvainOld.from_file("data/karate.txt")
        partition, q = pyl.apply_method()
        q_ = q * 10000
        print("PARTITON IS " , partition)
        

    def test_lesmis(self):
        pyl = PyLouvain.from_gml_file("data/lesmis.gml")
        partition, finalPartit, q = pyl.apply_method()

    def test_polbooks(self):
        pyl = PyLouvain.from_gml_file("data/polbooks.gml")
        partition, finalPartit, q = pyl.apply_method()

if __name__ == '__main__':
    unittest.main()
