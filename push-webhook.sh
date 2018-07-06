#!/bin/sh
url=ADD_URL
request="
{
    \"text\": \"text\",
    \"attachments\": [
        {
            \"fallback\": \"fallback\",
            \"author_name\": \"author_name\",
            \"title\": \"title\",
            \"text\": \"text\"
        }
    ]
}"

echo $request
