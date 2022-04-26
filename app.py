from datetime import datetime
from flask import Flask, request, render_template
from inference import get_category, plot_category

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissor():
    # Write the GET Method to get the index file
    if request.method == 'GET':
        return render_template('index.html')
    # Write the POST Method to post the results file
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('File Not Uploaded')
            return
        # Read file from upload
        file = request.files['file']
        # Get category of prediction
        category = get_category(img=file)
        # Plot the category
        now = datetime.now()
        current_time = now.strftime("%H-%M-%S")
        plot_category(file, current_time)
        # Render the result template
        return render_template('result.html', category=category, current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
