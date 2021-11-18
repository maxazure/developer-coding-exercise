import {Link} from "umi"
const PostList: React.FC<{ posts: API.PostListItem[]; }> = ({posts }) => {
  return (
      <ul>
        {
          posts.length > 0 && posts.map(post =>
            <li key={post.id}><Link to={`posts/${post.slug}`}>{post.title}</Link></li>)
        }
      </ul>
  );
};

export default PostList;
