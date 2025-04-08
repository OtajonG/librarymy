// Load books dynamically from Flask
function loadPDFs() {
  fetch("/list_pdfs")
    .then((response) => response.json())
    .then((data) => {
      let bookList = document.getElementById("bookList");
      bookList.innerHTML = "";

      data.forEach((pdf) => {
        let listItem = document.createElement("li");
        listItem.className =
          "list-group-item d-flex justify-content-between align-items-center";

        let link = document.createElement("a");
        // Ensure uploadsBaseUrl is defined before using it
        if (typeof uploadsBaseUrl !== 'undefined') {
          link.href = uploadsBaseUrl + pdf;
        } else {
          console.error("Error: uploadsBaseUrl is not defined. Cannot create PDF link.");
          link.href = "#"; // Or some other default/error URL
        }
        link.textContent = pdf;
        link.target = "_blank";
        link.className = "text-decoration-none";

        listItem.appendChild(link);
        bookList.appendChild(listItem);
      });
    })
    .catch((error) => console.error("Error loading PDFs:", error));
}

// Filter books by title
function filterBooks() {
  let query = document.getElementById("searchQuery").value.toLowerCase();
  let books = document.querySelectorAll("#bookList li");

  books.forEach((book) => {
    book.style.display = book.textContent.toLowerCase().includes(query)
      ? "flex"
      : "none";
  });
}

// Search inside PDFs
function searchPDFContent() {
  let query = document.getElementById("contentSearchQuery").value;

  fetch("/search_pdf_text", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: query }),
  })
    .then((response) => response.json())
    .then((data) => {
      let books = document.querySelectorAll("#bookList li");

      books.forEach((book) => {
        book.style.display = data.includes(book.textContent)
          ? "flex"
          : "none";
      });
    })
    .catch((error) => console.error("Error searching content:", error));
}

// Load PDFs on page load
window.onload = loadPDFs;