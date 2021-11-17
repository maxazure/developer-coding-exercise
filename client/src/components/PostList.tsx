const PostList: React.FC<{ posts: unknown[]; }> = ({posts }) => {
  return (
      <ul>
        {
          posts.map(post =>
            <li><a href={'posts/' + post.url}>{post.title}</a></li>)
        }
      </ul>
  );
};

export default PostList;