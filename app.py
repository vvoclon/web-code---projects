from flask import Flask, render_template
import main1
import jinja2


app = Flask(__name__)


@app.route('/')
def stat_web():
    return render_template("stats_web.html")

@app.route('/table/')
def table():

    headings = ["Schizophrenia", "Bipolar disorder", "Eating disorders", "Anxiety", "Drugs", "Depression",
                    "Alcohol"]
    data = main1.table_shapiro_result
    data_1 = main1.table_wilcoxon_result_tu
    desc_stat_data = main1.table_descriptive_stats
    headings_2 = ["", "", "Schizophrenia", "Bipolar disorder", "Eating disorders", "Anxiety", "Drugs", "Depression",
                    "Alcohol"]

    return render_template("Projekt 1.html.jinja", headings=headings, data=data, data_1=data_1, headings1=headings, desc_data=desc_stat_data, headings2 = headings_2)


def table():
    headings_1 = ["Schizophrenia", "Bipolar disorder", "Eating disorders", "Anxiety", "Drugs", "Depression",
                "Alcohol"]
    data_1 = main1.table_wilcoxon_result_tu
    
    return render_template("Projekt 1.html.jinja", headings=headings_1, data=data_1)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
