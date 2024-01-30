import os
from bs4 import BeautifulSoup
import networkx as nx

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(file.read(), 'html.parser')

        # Extract all links from the page
        links = [a.get('href') for a in soup.find_all('a', href=True)]

        return links

def build_graph(directory):
    # Create a directed graph using NetworkX
    G = nx.DiGraph()

    # Iterate through all HTML files in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.html'):
            file_path = os.path.join(directory, file_name)

            # Extract links from the HTML file
            links = extract_links(file_path)

            # Add edges to the graph based on extracted links
            for link in links:
                G.add_edge(file_name, link)

    return G

def compute_pagerank(graph):
    # Use NetworkX's pagerank function
    pagerank = nx.pagerank(graph)

    return pagerank

def analyze_directory(directory):
    # Build a directed graph from HTML files in the directory
    graph = build_graph(directory)

    # Compute pagerank for each page in the graph
    pagerank = compute_pagerank(graph)

    # Return a dictionary of HTML files mapped to their pagerank values
    return {page: float(score) for page, score in pagerank.items()}

if __name__ == "__main__":
    # Replace 'your_directory' with the actual directory path containing HTML files
    directory_path = '/path/to/your/directory'

    # Analyze the HTML files in the directory and get the result
    result = analyze_directory(directory_path)

    if result:
        # Print the result
        print("Result:")
        for page, score in result.items():
            print(f"{page}: {score}")
    else:
        print(f"No HTML files found in the directory {directory_path}")