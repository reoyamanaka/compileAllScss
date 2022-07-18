from unittest import TestCase, main
from utils import checkIfScss


class TestCheckIfSss (TestCase):
    def test_checkIfScss (self):
        self.assertEqual (checkIfScss ("asdfasfaf"), False)
        self.assertEqual (checkIfScss ("asdf.pdf"), False)
        self.assertEqual (checkIfScss ("asdf.pdf.scss"), True)
        self.assertEqual (checkIfScss ("asdf.scss"), True)
        self.assertEqual (checkIfScss ("asdf.scss.asdf"), False)


if __name__ == "__main__":
    main ()
