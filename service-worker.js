 importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.1.1/workbox-sw.js');
 if (workbox) {
   console.log('[ PWA Fire Bundle ] Hello from Workbox');


    workbox.routing.registerRoute(
       new RegExp('talks/'),
       new workbox.strategies.StaleWhileRevalidate({
         cacheName: 'talks/',
         plugins: [
          new workbox.cacheableResponse.Plugin({
           statuses: [0, 200],
          }),
          new workbox.expiration.Plugin({
           maxAgeSeconds: 60 * 60 * 24 * 1,
          }),
        ],
      })
    );
    


   workbox.core.skipWaiting();
   workbox.core.clientsClaim();
 } else {
   console.log('Boo! Workbox failed to load 😬');
 }