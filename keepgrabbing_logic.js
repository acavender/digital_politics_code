let i = 0;
// Most programming languages start counting from 0. We can check before we start and confirm that https://www.jstor.org/stable/pdf/0.pdf doesn't exist (it returns a 404 error), but https://www.jstor.org/stable/pdf/1.pdf *does* exist. Since we need to start our count with 1, we'll make 1 the first item in our mock database (represented here as an array.)

let articles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
// The array defined in the line above represents a mock database. If we were connecting to an actual database, we'd instead use code that connects us to that database.

while (i < articles.length) {
    // The line above checks to see whether we've already downloaded the final item in the mock database. If we haven't, the next line of code runs. If we have, the loop ends, and line 17 runs. The benefit of using a while loop here is that it will work with a database of any length, so we don't need to know in advance how many items there are. The loop will keep running until it runs out of items.

    console.log(`Download the article with the filename ${articles[i]}.pdf.`);
    // If we were querying a real article database, we'd issue an actual download command.

    i++;
    // The line above increases the index by one and starts the while loop again.
}

console.log("No more articles to download.");

