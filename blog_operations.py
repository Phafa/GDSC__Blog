from Blogapp.models import post
from CommentApp.models import comment

#create post
post1  = post.objects.create(
    title="post 1 Title",
    content="content of post 1",
    category="category 1",
    image="image1.jpg",
    tags=["tag1", "tag2"],
)

post2 = post.objects.create(
    title="post 2 Title",
    content="content of post 2",
    category="category 2",
    image="image2.jpg",
    tags=["tag3"],
)

post3 = post.objects.create(
    title="post 3 Title",
    content="content of post 3",
    category="category 3",
    image="image3.jpg",
    tags=["tag1", "tag4"],
)

# Query posts by category
category_posts = Post.objects.filter(category="Category 1")
print("Posts in category 1:")
for post in category_posts:
    print(post.title)

# Update post content
post1.content = "Updated content for post 1"
post1.save()

# Delete a post
post1.delete()

# Create comments
comment1 = Comment.objects.create(
    content="This is comment 1", author="John Doe", post=post1
)
comment2 = Comment.objects.create(
    content="This is comment 2", author="Jane Doe", post=post3
)
comment3 = Comment.objects.create(
    content="This is comment 3", author="Alice", post=post1
)

# Query comments by post
post1_comments = Comment.objects.filter(post=post1)
print("\nComments on post 1:")
for comment in post1_comments:
    print(f"{comment.author}: {comment.content}")

# Update comment content
comment2.content = "Updated comment content"
comment2.save()

# Delete a comment
comment1.delete()

