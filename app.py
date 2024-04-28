from flask  import Flask, request

app = Flask(__name__)

#create the idea repository
ideas = {
    1 : {
        "id": 1,
        "idea_name": "ONDC",
        "idea_description": "Details about ONDC",
        "idea_author": "Aman"
    },
    2 : {
        "id": 2,
        "idea_name": "Save soil",
        "idea_description": "Details about saving soil",
        "idea_author": "Shubhankar"
    }
}

"""
create a RESTful endpoint for fetching all the ideas
"""
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    idea_author = request.args.get('idea_author')

    if idea_author:
        idea_res = {}
        for key, value in ideas.items():
            if value['idea_author'] == idea_author:
                idea_res[key] = value
        return idea_res

    #logic to fetch all the ideas
    return ideas

"""
Create a RESTful endpoint to create a new idea
"""
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    #logic to create new idea
    try:
        #first read the request body
        request_body = request.get_json()

        #check if the idea id passed is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with the same id already present",400

        #insert the passed idea in the ideas dict
        ideas[request_body["id"]] = request_body

        #return the response saying idea got saved
        return "idea created and saved",201
    except KeyError:
        return "id is missing",400
    except:
        return "some internal server error",500


"""
endpoint to fetch idea based on idea id
"""
@app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_ideas_by_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return "some internal error happened",500


"""
endpoint for updating the idea
"""
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
    except:
        return "some internal error happened",500


"""
endpoint to delete an idea
"""
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return "idea got successfully deleted",200
        else:
            return "idea id passed is not present",400
    except:
        return "some internal error happened",500



if __name__ == '__main__':
    app.run(port=8080)