from gmplot import *
import webbrowser
import RabinKarp
import chart_studio.plotly as py
import plotly.graph_objs as go
import time
from sys import maxsize
import copy
from geopy.geocoders import Nominatim
from geopy import distance

start = time.time()
geolocator = Nominatim(user_agent="Algo Assignment", timeout=30)
# --------------------------------------------------Question 1-------------------------------------------------------------------#

cities = ['Kuala Lumpur', 'Jakarta', 'Bangkok', 'Taipei', 'HongKong', 'Beijing', 'Tokyo', 'Seoul']
cities_latitude = [None] * len(cities)
cities_longitude = [None] * len(cities)
for i in range(len(cities)):
    location = geolocator.geocode(cities[i], timeout=150)
    cities_latitude[i] = location.latitude
    cities_longitude[i] = location.longitude

gmap2 = gmplot.GoogleMapPlotter(14.794071, 120.992590, 4)
gmap2.scatter(cities_latitude, cities_longitude, '#FF0000', size=70000, marker=False)
gmap2.apikey = "AIzaSyCcMbBJ6orBWY5-Zswb8BJnUdBfh_bcYiU"
gmap2.draw("maps/plotted.html")
url = r"maps\plotted.html"
webbrowser.open(url, new=2)

# -------------------------------------------------Question 2-------------------------------------------------------------------#

cities_location = {}
cities_coords = {}
cities_distance = {}

for i in range(len(cities)):
    cities_location[cities[i]] = geolocator.geocode(cities[i])
    cities_coords[cities[i]] = {}

for i in range(len(cities)):
    cities_coords[cities[i]]['latitude'] = cities_location[cities[i]].latitude
    cities_coords[cities[i]]['longitude'] = cities_location[cities[i]].longitude


def calcdistance(start):
    for i in range(0, len(cities)):
        cities_distance[cities[start]][cities[i]] = int(
            distance.distance((cities_coords[cities[start]]['latitude'], cities_coords[cities[start]]['longitude']),
                              (cities_coords[cities[i]]['latitude'], cities_coords[cities[i]]['longitude'])).kilometers)
        print(cities[start] + '<->' + cities[i] + "\n" + "Distance :" + str(cities_distance[cities[start]][cities[i]]))
        if i % 7 == 0 and i > 0:
            print('\n')


for i in range(len(cities)):
    cities_distance[cities[i]] = {}
    calcdistance(i)

# -------------------------------------------------Question 3,4------------------------------------------------------------------#


class TravellingSalesman():
    def __init__(self, graph, s, t):
        # store all vertex apart from source vertex
        self.route = [s]
        dummy_graph = copy.deepcopy(graph)
        dummy_country = copy.deepcopy(cities)

        for i in range(len(dummy_country)):
            dummy_graph[i].append(0)
            if i == s:
                dummy_graph[i].append(0)
            else:
                dummy_graph[i].append(maxsize)

        dummy_country.append("All")
        dummy_country.append("StartEnd")
        dummy_graph.append([0] * len(dummy_country))
        dummy_graph.append([0])
        for i in range(len(dummy_country) - 2):
            dummy_graph[len(dummy_country) - 1].append(maxsize)
        dummy_graph[len(dummy_country) - 1].append(0)

        vertex = []
        for i in range(len(dummy_graph)):
            if i != s:
                vertex.append(i)

        # store minimum weight Hamiltonian Cycle
        min_path = maxsize

        while True:

            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = s
            current_route = dummy_country[s]
            test_route = [dummy_country[s]]

            for i in range(len(vertex)):
                current_pathweight += dummy_graph[k][vertex[i]]
                k = vertex[i]
                if (dummy_country[k] != "StartEnd") and (dummy_country[k] != "All"):
                    current_route += "-->" + dummy_country[k]
                    test_route.append(dummy_country[k])
            current_pathweight += dummy_graph[k][s]

            # update minimum
            if current_pathweight < min_path:
                shortest_route = current_route
                self.route = test_route
            min_path = min(min_path, current_pathweight)

            if not next_permutation(vertex):
                break

        print("Best Route:", shortest_route,"\nDistance:", min_path, "km\n")
        l = shortest_route.split('-->')
        t += l

        storeLatCor = []
        storeLongCor = []
      

        for i in range(len(cities)):
            mark = geolocator.geocode(l[i])
            storeLatCor.append(mark.latitude)
            storeLongCor.append(mark.longitude)

        gmap3 = gmplot.GoogleMapPlotter(14.794071, 120.992590, 4)

        gmap3.scatter(cities_latitude, cities_longitude, '#FF0000', size=100, marker=False)
        gmap3.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
        gmap3.marker(cities_latitude[0], cities_longitude[0], 'cornflowerblue')

        for j in range(len(cities) + 1):
            for i in range(len(cities) + 1):
                gmap3.plot(storeLatCor[j:i], storeLongCor[j:i], 'black', edge_width=2.5)

        gmap3.apikey = "AIzaSyCcMbBJ6orBWY5-Zswb8BJnUdBfh_bcYiU"
        gmap3.draw("maps/shortest.html")

        url = r"maps\shortest.html"
        webbrowser.open(url, new=2)

        return None

    def get_route(self):
        return self.route


# next_permutation implementation
def next_permutation(L):
    n = len(L)
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

t = []
# matrix representation of graph
adj = [[0 for i in range(len(cities))] for j in range(len(cities))]
for i in range(len(cities)):
    for j in range(len(cities)):
        adj[i][j] = cities_distance[cities[i]][cities[j]]
s = 0
TravellingSalesman(adj, s, t)


# -------------------------------------------------Question 5-------------------------------------------------------------------#

prePath = "C:/Users/user/PycharmProjects/Assignment/news/"
cities1 = ['Jakarta', 'Bangkok', 'Taipei', 'HongKong', 'Beijing', 'Tokyo', 'Seoul']

py.sign_in(username='miszsimple', api_key='tLoEammky5Hg8YrrGkxg')

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
             'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
             'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did',
             "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few',
             'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
             'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
             'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
             'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
             'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
             'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd",
             "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's",
             'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under',
             'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
             'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
             "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves']


def word_count(text):
    stop_count = 0
    list_of_words = text.split()
    for word in stopwords:
        if RabinKarp.rabin_karp_matcher(word, text):
            stop_count = stop_count + 1
            # delete stop words
            text = text.lower().replace(word, "", 1)
    return stop_count, len(list_of_words)


stop = []
total = []
for i in cities1:
    stop1 = 0
    total1 = 0
    for j in range(5):
        file = open(prePath + i + str(j + 1) + ".txt", encoding="utf8")
        text = file.read().lower()
        text = text.replace("\n", " ")
        file.close()
        stop_count, total_word = word_count(text)

        stop1 += stop_count
        total1 += total_word

    stop.append(stop1)
    total.append(total1)
# -------------------------------------------------Question 6-------------------------------------------------------------------#
x = ["Jakarta", "Bangkok", "Taipei", "HongKong", "Tokyo", "Beijing", "Seoul"]
stop_counts = stop
total_words = total

data = [
    go.Histogram(
        histfunc="sum",
        y=stop_counts,
        x=x,
        name="Stop words"
    ),
    go.Histogram(
        histfunc="sum",
        y=total_words,
        x=x,
        name="Total words"
    )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Stop Words & Total Words",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    xaxis_title='Places',  # xaxis label
    yaxis_title='Word Count',  # yaxis label
    bargap=0.2,  # gap between bars of adjacent location coordinates
    bargroupgap=0  # gap between bars of the same location coordinates
)
py.plot(fig)
# -------------------------------------------------Question 7-------------------------------------------------------------------#
positive_word = open('wordlist/positivewords.txt', 'r', encoding='utf-8')
positive_text = positive_word.read().lower().split('\n')

negative_word = open('wordlist/negativewords.txt', 'r', encoding='utf-8')
negative_text = negative_word.read().lower().split('\n')


# getting the frequency of positive, negative and neutral words in a text
def wordcount(text):
    total_length = len(text.split())
    count = 0
    positive = 0
    negative = 0

    for pat in positive_text:
        pat = pat.replace(" ", "")
        if RabinKarp.rabin_karp_matcher(pat, text):
            positive = positive + 1
            count = count + 1
    for pat in negative_text:
        pat = pat.replace(" ", "")
        if RabinKarp.rabin_karp_matcher(pat, text):
            negative = negative + 1
            count = count + 1
    return positive, negative


posword = []
negword = []
for i in cities1:
    pos = 0
    neg = 0
    for j in range(5):
        file = open(prePath + i + str(j + 1) + ".txt", encoding="utf8")
        text = file.read().lower()
        text = text.replace("\n", " ")
        file.close()
        Positive, Negative = wordcount(text)
        print("Postive  :", Positive)
        print("Negative :", Negative)
        pos += Positive
        neg += Negative
    posword.append(pos)
    negword.append(neg)


# -------------------------------------------------Question 8----------------------------------------------------------------#

x = ["Jakarta", "Bangkok", "Taipei", "HongKong", "Tokyo", "Beijing", "Seoul"]
positive_y = posword
negative_y = negword

data = [
    go.Histogram(
        histfunc="sum",
        y=positive_y,
        x=x,
        name="Positive words"
    ),
    go.Histogram(
        histfunc="sum",
        y=negative_y,
        x=x,
        name="Negative words"
    )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Positive and Negative words in articles",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    xaxis_title='Places',  # xaxis label
    yaxis_title='Word Count',  # yaxis label
    bargap=0.2,  # gap between bars of adjacent location coordinates
    bargroupgap=0  # gap between bars of the same location coordinates
)
py.plot(fig)



# -------------------------------------------------Question 9----------------------------------------------------------------#
def sentiment(positive_frequency, negative_frequency, city):
    print("\n" + city)
    if positive_frequency > negative_frequency:
        print('The article is giving positive sentiment with ratio ' + (str(positive_frequency / negative_frequency)))
        print('So the country has positive economic/financial situation')
    elif negative_frequency > positive_frequency:
        print('The article is giving negative sentiment with ratio ' + (str(negative_frequency / positive_frequency)))
        print('So the country has negative economic/financial situation')


print("\n\nConcluding the cities' economic/financial situation")
for i in range(len(posword)):
    sentiment(posword[i], negword[i], x[i])
# -------------------------------------------------Question 10----------------------------------------------------------------#
difposneg = []

for i in range(len(posword)):
    difposneg.append(posword[i] - negword[i])

x = ["Jakarta", "Bangkok", "Taipei", "HongKong", "Tokyo", "Beijing", "Seoul"]
positive_y = difposneg

data = [
    go.Histogram(
        histfunc="sum",
        y=positive_y,
        x=x,
        name="Difference"

    )

]
layout = go.Layout(
    title=go.layout.Title(
        text="The Total of Positive and Negative Sentiment of Article",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    xaxis_title='Places',  # xaxis label
    yaxis_title='Difference between positive and negative words',  # yaxis label
    bargap=0.2,  # gap between bars of adjacent location coordinates
    bargroupgap=0  # gap between bars of the same location coordinates
)
py.plot(fig)
end = time.time() - start
print("Total running time: " + str(end) + "s")
