from unittest import TestCase, main
from utils import checkIfScss, getNameWithoutScssExtension


class TestUtils (TestCase):
    def test_checkIfScss (self):
        self.assertEqual (checkIfScss ("asdfasfaf"), False)
        self.assertEqual (checkIfScss ("asdf.pdf"), False)
        self.assertEqual (checkIfScss ("asdf.pdf.scss"), True)
        self.assertEqual (checkIfScss ("asdf.scss"), True)
        self.assertEqual (checkIfScss ("asdf.scss.asdf"), False)
    
    def test_getNameWithoutScssExtension (self):
        self.assertEqual (getNameWithoutScssExtension ("asdf.pdf"), "asdf.pdf")
        self.assertEqual (getNameWithoutScssExtension ("asdf.pdf.scss"), "asdf.pdf")
        self.assertEqual (getNameWithoutScssExtension ("asdf"), "asdf")
        self.assertEqual (getNameWithoutScssExtension ("asdf.scss.scss"), "asdf.scss")


if __name__ == "__main__":
    main ()
