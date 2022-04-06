console.log("hello world")

const APILink = "http://127.0.0.1:8000/"

let emotionSelect = document.getElementById("emotion");
let genreSelect = document.getElementById("genre");

let emotions = []
async function getEmotions(){
    query = APILink+"annotations"
    const response = await fetch(query);
    emotions = await response.json();
    emotions['annotations'].forEach(emotion => {
    option = document.createElement("option");
    option.value = emotion;
    option.text = emotion;
    emotionSelect.appendChild(option)
})
}
getEmotions();

async function populateTable(query) {
    console.log("populate");
    reviewTable = document.getElementById("review-table")
    reviewTable.innerHTML = '';
    const response = await fetch(query);
    let reviews = await response.json();
    reviews['reviews'].forEach(review =>{
        tableRow = document.createElement("tr");

        titleCell = document.createElement("td");
        titleCell.innerHTML = review['title'];
        tableRow.appendChild(titleCell);

        authorCell = document.createElement("td");
        authorCell.innerHTML = review['author'];
        tableRow.appendChild(authorCell);

        genreCell = document.createElement("td");
        genreCell.innerHTML = review['genre'];
        tableRow.appendChild(genreCell);

        ratingCell = document.createElement("td");
        ratingCell.innerHTML = review['rating'];
        tableRow.appendChild(ratingCell);

        reviewCell = document.createElement("td");
        reviewDiv = document.createElement("div");
        reviewDiv.classList.add("review");
        reviewDiv.classList.add("overflow-scroll");
        reviewDiv.innerHTML = review['review'];
        reviewCell.appendChild(reviewDiv);
        tableRow.appendChild(reviewCell);

        emotionCell = document.createElement("td");
        emotionCell.innerHTML = review['emotion'];
        tableRow.appendChild(emotionCell);

        reviewTable.appendChild(tableRow);

    })
}

populateTable(APILink+'reviews');

let genres ; 
async function getGenres() {
    query = APILink+"genres"
    const response = await fetch(query);
    genres = await response.json();
    genres['genres'].forEach(genre => {
        option = document.createElement("option");
        option.value = genre;
        option.text = genre;
        genreSelect.appendChild(option)
    })
}
getGenres(); 

var submit = document.getElementById("submit");

submit.addEventListener("click", async function () {
    console.log("submit")
    let title = document.getElementById("book-title").value;
    let author = document.getElementById("author-name").value;
    let rating = document.getElementById("rating").value;
    let genre = genreSelect.value;
    let emotion = emotionSelect.value;
    let query = APILink+'search'+"?"
    if (title){
        query += "title="+title+"&";
    }
    if (author){
        query += "author="+author+"&";
    }
    if (rating){
        query += "rating="+rating+"&";
    }
    if (genre){
        query += "genre="+genre+"&";
    }
    if (emotion){
        query += "emotion="+emotion+"&"
    }
    query = query.slice(0, -1);
    console.log(query)
    await populateTable(query);
    if (document.getElementById("review-table").childElementCount == 0){
        no_reviews = reviewCell = document.createElement("div");
        no_reviews.classList.add("alert");
        no_reviews.classList.add("alert-dark");
        no_reviews.innerHTML = "There are no reviews in our database which match the current filters";
        reviewTable = document.getElementById("review-table");
        reviewTable.appendChild(no_reviews);
    }

    
  });