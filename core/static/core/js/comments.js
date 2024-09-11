//keeps track of what comment page user is on, default = 1
let commentPage = 1


function getPage(page) {
    const response = fetch(window.location.origin + `/api/comments/${POST_ID}/${page}`)
                        .then(response => response.json())
    return response
}

//removes everything, but author, content and creation date
function processComments(comments) {
    const processedComments = []
    for(const comment of comments) {
        const stripped_comment = {}
        for(const field in comment.fields) {
            if(field == "post") continue
            stripped_comment[field] = comment.fields[field]
        }
        stripped_comment.id = comment.pk
        processedComments.push(stripped_comment)
    }
    return processedComments
}

function displayComments(comments) {
    const commentsContainer = document.querySelector(".comments-container")
    for(const comment of comments) {
        const commentDiv = document.createElement("div")
        commentDiv.classList.add("comment-div");
        
        const headerDiv = document.createElement("div")
        headerDiv.classList.add("comment-header-div")

        const contentDiv = document.createElement("div")
        contentDiv.classList.add("comment-content-div")


        const authorSpan = document.createElement("span")
        authorSpan.classList.add("author-span")
        const authorAnchorTag = document.createElement("a")
        authorAnchorTag.href = `/profile/${comment.author}`
        const author = document.createTextNode(comment.author)
        authorAnchorTag.appendChild(author)
        authorSpan.appendChild(authorAnchorTag)
        

        const creationDateSpan = document.createElement("span")
        creationDateSpan.classList.add("creation-date-span")
        const creationDate = document.createTextNode(comment.created_on)
        creationDateSpan.appendChild(creationDate)

        const contentSpan = document.createElement("span")
        contentSpan.classList.add("content-span")
        const content = document.createTextNode(comment.content)
        contentSpan.appendChild(content)


        headerDiv.appendChild(authorSpan)
        headerDiv.appendChild(creationDateSpan)

        contentDiv.appendChild(contentSpan)

        commentDiv.appendChild(headerDiv)
        commentDiv.appendChild(contentDiv)
        commentDiv.dataset.id = comment.id
        commentDiv.dataset.author = comment.author

        commentsContainer.appendChild(commentDiv)
    }
}

function updateFooter() {
    document.querySelector(".current-page").innerHTML = commentPage
}

function addEventListenerToFooter() {
    const previous = document.querySelector(".previous-page")
    const next = document.querySelector(".next-page")

    previous.addEventListener("click", (e) => {
        if (commentPage > 1) commentPage -= 1
        main()
    })

    next.addEventListener("click", (e) => {
        commentPage += 1
        main()
    })
}

function clearCommentContainer() {
    document.querySelector(".comments-container").innerHTML = ""
}


function appendDeleteCommentBtn() {
    comments = document.querySelectorAll(".comment-header-div");
    for(let comment of comments) {
        if(comment.parentElement.dataset.author == user || superuserStatus == "True") {
            deleteBtn = document.createElement("a");
            deleteBtn.classList.add("delete-btn");
            deleteBtn.appendChild(document.createTextNode("Delete"))

            deleteBtn.addEventListener("click", async function handleClick(e) {
                const commentId = e.srcElement.parentElement.parentElement.dataset.id;
                response = await fetch(window.location.origin + `/api/comments/delete/${commentId}`)
                if(response.status == 200) {
                    this.innerHTML = "Deleted!";
                }
            })
            comment.appendChild(deleteBtn);
        }
    }
}


async function main() {
    let comments;
    try { comments = await getPage(commentPage) }
    catch { commentPage -= 1; return; }
    console.log(comments);
    const processedComments = processComments(comments)
    console.log(processedComments);
    clearCommentContainer()
    displayComments(processedComments)
    appendDeleteCommentBtn()
    updateFooter()
}


main()
addEventListenerToFooter()
