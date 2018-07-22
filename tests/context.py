import sys
import os
from aness.app import AlterDecoy

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), '..')))

app = AlterDecoy()
