from density_calculator import DensityCalculator
from tokenizer import Tokenizer
from filters import StopwordsFilter

calculator = DensityCalculator(Tokenizer(), StopwordsFilter('en'))

densities = calculator(''' To follow along with future lessons it is important that you have the right files and programs in your programming-historian directory. At the end of each lesson in this series you can download the programming-historian zip file to make sure you have the correct code.''')

print densities
