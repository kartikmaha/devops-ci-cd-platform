##FROM nginx:alpine
FROM public.ecr.aws/nginx/nginx:alpine
# Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# Copy our static HTML page
COPY index.html /usr/share/nginx/html/

# Expose HTTP port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
