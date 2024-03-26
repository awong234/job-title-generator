#!Rscript
library(jsonlite)

if (file.exists('words.json')) {
    words <- jsonlite::fromJSON("words.json")
} else {
    words <- jsonlite::fromJSON("https://raw.githubusercontent.com/awong234/job-title-generator/main/words.json")
}

generate_job_title = function(choices = NULL) {
    if (is.null(choices)) {
        choices = c("prefix", "adjective", "superlative", "job type", "title", "suffix")
        # Sample from the space of choices, turn on and off randomly
        selection = sample(x = c(TRUE, FALSE), size = length(choices), replace = TRUE)
        names(selection) = choices
        # But keep job type active
        selection['job type'] = TRUE
        choices = choices[selection]
    }
    # Pick randomly from each category
    my_sample = sapply(X = choices, FUN = \(x) sample(words[[x]], size = 1))
    rank = sample(c(1:29), size = 1) |> as.roman()
    out = paste0( my_sample , collapse = ' ')
    out = paste(out, rank)
    out
}

cat(generate_job_title(), '\n')

# titles = vector(mode = 'character', length = 1000)
# for (i in 1:1000) {
#     set.seed(i)
#     titles[i] = generate_job_title()
#     cat(i, '\t', titles[i], '\n')
# }

# titles_df = data.frame(
#     seed = 1:1000,
#     titles
# )

# Titles sorted by length
# titles_df[order(titles_df$titles |> nchar()), ]
