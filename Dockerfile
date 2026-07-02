FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html guide.html tips.html faq.html blog.html blog-write.html robots.txt sitemap.xml ./
COPY css ./css
COPY js ./js
COPY config ./config
COPY data ./data
COPY blog ./blog
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
