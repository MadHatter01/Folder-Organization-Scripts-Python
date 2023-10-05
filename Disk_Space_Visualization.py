import os;
import matplotlib.pyplot as plt;
import plotly.express as px;


def analyze_disk(directory):
    sizes, labels = [], []
    data = []

    for root, directories, files in os.walk(directory):
        folder_size = sum(os.path.getsize(os.path.join(root, filename)) for filename in files)
        if folder_size > 0:
            sizes.append(folder_size)
            labels.append(root)
            data.append({'Directory':root, 'Size (MB)': folder_size/ (1024**2)})

    return sizes, labels, data


def plot_fcn(sizes, labels):
    plt.figure(figsize=(10,6))
    plt.barh(labels, sizes, color='skyblue')
    plt.xlabel('Disk Space')
    plt.ylabel('Directory')
    plt.title('Disk Space Usage (Folders)')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    sizes, labels, data = analyze_disk('C:/Users/vaish/Documents/Development/')
    print(sizes, labels)
    if data:
        fig = px.treemap(data, path=['Directory'], values='Size (MB)', title='Disk Space Usage (Folders)');
        fig.update_traces(textinfo="label+value");
        fig.show()
    else:
        print("No data to show")
    # plot_fcn(sizes, labels)
