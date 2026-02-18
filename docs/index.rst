.. PlumeIA-API documentation master file, created by
   sphinx-quickstart on Tue Feb 17 15:48:03 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation des APIs
=============================================

Notre plateforme propose plusieurs interfaces de programmations applicatives (API) permettant d'interagir facilement avec nos services. 

Les API sont conçues pour être simples à utiliser, sécurisées et fiables. Elles requièrent une authentification 
via des en-têtes HTTP et renvoient des réponses au format JSON standardisé.

Consultez la documentation détaillée de chaque API :

.. toctree::
   :maxdepth: 2
   
   api


Authentification
~~~~~~~~~~~~~~~~~~~~
Tous les points de terminaison requiert une clé APU fourni par Plume à votre organization.

Codes d'erreurs
~~~~~~~~~~~~~~~~~~~~
Les erreurs utilisent les codes standards HTTP. Par exemple:

- `400 Bad Request` – Entrée non valide 
- `401 Unauthorized` – Clé API manquante ou non valide
- `404 Not Found` –  Ressource inexistante  
- `500 Internal Server Error` – Erreur côté serveur
