from os import system,path
from facebook_scraper import get_posts
import warnings


class scbook:
    def logo(self):
        print("""

    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ ██████╗  ██████╗  ██████╗ ██╗  ██╗
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║██║   ██║█████╔╝ 
    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║   ██║██╔═██╗ 
    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
      who said that you need a facebook account and no privacy to stalk someone on facebook?
                              \033[3m·proudly developed by kl3sshydra·\033[0m

        """)

    def getoptions(self):
        target = input("insert profile name: ")
        fname = target+".html"
        filename = input(f"insert output filename (default: {fname}): ")
        np = 1
        npages = input("insert page number (default: 1): ")
        if npages != "":
            try:
                np = int(npages)
            except:
                print("invalid pages number provided.")
                pass
        if filename != "":
            fname = filename
        return [target, fname, np]

    def scrapeposts(self,profilename,pages):
        postlist = list()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for post in get_posts(profilename, pages=pages):
                postlist.append(post)
        return postlist

    def parsesinglepost(self,post_content):
        print(f"""
------- Scraping new post -------
POST URL: {post_content['post_url']}
POST CAPTION: {post_content['text']}
POST IMAGE URL: {post_content['image']}
COMMENT COUNT: {post_content['comments']}
SHARE COUNT: {post_content['shares']}
LIKE COUNT: {post_content['likes']}
""")

    def writetohtmlfile(self, htmlfilename,target,pagenumber,postlist):
        if path.exists(htmlfilename) == False:
            f = open(htmlfilename,"a")
            f.write(f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <style>
        div {{
            background-color: blue;
            color: aliceblue;
        }}
        
        .singlepost {{
            background-color: black;
            color: white;
        }}
    </style>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ScraperBook - {target}</title>
</head>

<body>

    <div>ScraperBook output file for target {target} -> {str(pagenumber)} pages </div>
        """)

        for post in postlist:
            scbook.parsesinglepost(post)
            f.write(f"""
<br>
    <div class="singlepost">
        <center>
            <h4>{post['post_url']}</h4>
            <img src={post['image']}>
            <h3>{post['likes']} likes - {post['shares']} shares - {post['comments']} comments</h3>
            <h5>{post['text']}</h5>
        </center>
    </div>""")

        f.close()



    def main(self):
        system("clear")
        scbook.logo()
        pf = scbook.getoptions()
        profile_ = pf[0]
        outfilename_ = pf[1]
        npages = pf[2]
        print(f"Starting against profile \"{profile_}\", with output \"{outfilename_}\" for {npages} pages")
        targetposts = scbook.scrapeposts(profile_, npages)
        scbook.writetohtmlfile(outfilename_,profile_,npages,targetposts)
            



scbook = scbook()
scbook.main()