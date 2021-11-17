declare namespace API {
    type Post = {
      id?: number;
      title?: string;
      slug?: string;
      author?: string;
      tags?: string;
      content?: string;
      created_on?: string;
    };
    type PostListItem = {
      id?: number;
      title?: string;
      url?: string;
      created_on?: string;
    };
  }