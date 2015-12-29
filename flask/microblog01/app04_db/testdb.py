from app04 import db, models

def insertData():
    u = models.User(nickname='john', email='john@email.com')
    db.session.add(u)
    db.session.commit()

    u = models.User(nickname='susan', email='susan@email.com')
    db.session.add(u)
    db.session.commit()

    users = models.User.query.all()
    print users
    for u in users:
        print u.id,u.nickname
         
    u = models.User.query.get(1)
    print u


    import datetime
    u = models.User.query.get(1)
    p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
    db.session.add(p)
    db.session.commit()



def queryData():
    # get all posts from a user
    u = models.User.query.get(1)
    print u
    
    posts = u.posts.all()
    print posts
    
    # obtain author of each post
    for p in posts:
        print p.id,p.author.nickname,p.body
    
    # a user that has no posts
    u = models.User.query.get(2)
    print u
    print u.posts.all()
    
    # get all users in reverse alphabetical order
    print models.User.query.order_by('nickname desc').all()


def deleteData():
    users = models.User.query.all()
    for u in users:
        db.session.delete(u)
    
    posts = models.Post.query.all()
    for p in posts:
        db.session.delete(p)
    
    db.session.commit()
