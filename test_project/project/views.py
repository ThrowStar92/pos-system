from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import numpy as np
import os
import json
from pathlib import Path
from django.conf import settings
import random

# Create your views here.
class home(APIView) :
    def get(self, request) :
        
        return Response()
    def custom_action(self,request):
        return Response({'message': 'Custom Action'})
    
    @classmethod
    def get_extra_actions(cls):
        return []