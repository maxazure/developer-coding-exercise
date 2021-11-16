"""Note: Running seed.py will delete all data records!!!
   seed.py is for testing purposes only
   ==================================================
   seed.py Used to initialize the database and store the text content of /assets/posts/*.md in the database
           In addition, it also get Tags by calculating the word frequency of nouns

   RUN:

   python seed.py

"""
from pathlib import Path
import django
import os
import re
import nltk

# To count the Part Of Speech(pos)
nltk.download('averaged_perceptron_tagger')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

django.setup()
# Must configure the Django environment variables before we import this model.
from posts.models import Post

def get_data_from_dir(target_dir, file_extension='.md'):
    """Read all (file_extension) type files in a folder and return the file content string array.
       Can only traverse one level, No subdirectories.

    Args:
        target_dir (string): The path of the destination folder
        file_extension (string): Optional, the type suffix of the target file

    Returns:
        Array: String array of all file contents
    """
    file_content_arr = []
    files = os.listdir(target_dir)

    # Traverse the folder and get the content of (*.md) files
    for file in files:
        if os.path.splitext(file)[1] == file_extension:
            try:
                with open(target_dir + file, 'r') as f:
                    file_content_arr.append(f.read())
                    f.close()
            except Exception as e:
                print(e)
    return file_content_arr


def calculate_tags(content):
    stopWords = [
        "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
        "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
        "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
        "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
        "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
        "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
        "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
        "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
        "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
        "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
        "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
        "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
        "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
        "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
        "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
        "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
        "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
        "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
        "yourself", "yourselves"
    ]

    # Another way to count common keywords
    # The result is not good, would do more research in the future
    #
    # r = Rake()
    # r.extract_keywords_from_text(content)
    # return r.get_ranked_phrases_with_scores()

    wordlist = []
    content = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', content.lower(), flags=re.MULTILINE)
    regex = r"[a-z|\'|\-]+"
    matches = re.finditer(regex, content, re.MULTILINE | re.IGNORECASE)

    for matchNum, match in enumerate(matches, start=1):
        if len(match.group()) > 2:
            wordlist.append(match.group())

    filtered_words = [word for word in wordlist if word not in stopWords]
    # Mark part of speech and leave only noun words
    pos_sequence = nltk.pos_tag(filtered_words)
    nounwords = [n for n, value in pos_sequence if value in ['NN']]

    # Calculate the frequency of nouns (Collections... is the implementation method)
    frequency = nltk.FreqDist(nounwords)  # collections.Counter(nounwords)

    # sorted(frequency.items(), key=lambda item:item[1], reverse=True)[:5]
    return [x for (x, y) in frequency.most_common(5)]


def main():
    POSTS_DIR = "{}/assets/posts/".format(Path(__file__).resolve().parent.parent)

    Post.objects.all().delete()

    # save the text of *.md to [Post] in the database
    for markdown_file in get_data_from_dir(POSTS_DIR):
        post = Post()
        post.deserializer(markdown_file)
        post.tags = ','.join(calculate_tags(post.title + post.content))
        post.save()
        print("Blog: [ {} ] has been added.".format(post.title))
        print("Tags: {}".format(post.tags))
        print("                          ")


if __name__ == "__main__":
    main()
