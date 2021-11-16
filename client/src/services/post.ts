// @ts-ignore
/* eslint-disable */
import { request } from 'umi';

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
}

declare namespace API {
  type PostListItem = {
    id?: number;
    title?: string;
    url?: string;
    created_on?: string;
  };
}

/** Get posts GET /api/posts */
export async function queryPostList() {
  return request<API.PostListItem>('/api/posts/', {
    method: 'GET',
  });
}

/** Get posts GET /api/post/xxx-xxx */
export async function queryPost(url: string) {
  if (url === undefined) {
    return null;
  }
  return request<API.Post>('/api/posts/' + url + '/');
}
