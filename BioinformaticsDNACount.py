import pandas as pd
import streamlit as sl
import altair as alt
from PIL import Image

image = Image.open('logo.png')
sl.image(image, use_column_width=True)
sl.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA
""")

sl.header('Enter DNA Sequence')

sequence_input = ">DNA QUERY 2 \n"