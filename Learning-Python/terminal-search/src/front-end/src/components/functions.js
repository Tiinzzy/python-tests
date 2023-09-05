export const PATTERN1 = /\d+\s+hours\s+ago/;
export const PATTERN2 = /\d+\s+week\s+ago/;
export const PATTERN3 = /\d+\s+hours\s+ago/;
export const PATTERN4 = /\d+\s+hour\s+ago/;

export function tableReadyData(allData) {
    let fullDetail = [];

    for (let i in allData.nltk_step_sentiment) {
        fullDetail.push({ 'index': allData.nltk_step_sentiment[i].title_index, 'title': allData.nltk_step_sentiment[i].title, 'nltk_sentiment': allData.nltk_step_sentiment[i].nltk_title });
    }

    for (let i in allData.text_blob_step_sentiment) {
        if (fullDetail[i].index === allData.text_blob_step_sentiment[i].title_index) {
            fullDetail[i]['blob_sentiment'] = allData.text_blob_step_sentiment[i].blob_title;
        }
    }

    for (let i in allData.vader_step_sentiment) {
        if (fullDetail[i].index === allData.vader_step_sentiment[i].title_index) {
            fullDetail[i]['vader_sentiment'] = allData.vader_step_sentiment[i].vader_title;
        }
    }

    fullDetail.forEach(obj => {
        obj.totalScore = 0;

        obj.totalScore += (obj.nltk_sentiment === 'Positive') ? 1 : (obj.nltk_sentiment === 'Negative') ? -1 : 0;
        obj.totalScore += (obj.blob_sentiment === 'Positive') ? 1 : (obj.blob_sentiment === 'Negative') ? -1 : 0;
        obj.totalScore += (obj.vader_sentiment === 'Positive') ? 1 : (obj.vader_sentiment === 'Negative') ? -1 : 0;
    })

    return fullDetail;
}