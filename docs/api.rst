APIs
======

get-upload-url
-----------------------
Cet API vous permet de demander un url vous permettant de télécharger un enregistrement dans le but de créer une transcription.
Le lien de téléchargemet sera valide pour une durée d'une heure. 

Points de terminaison
~~~~~~~~~~~~~~~~~~~~~~
- **POST https://fkaw8ao81j.execute-api.ca-central-1.amazonaws.com/dev/get-upload-url**  

Paramètres
~~~~~~~~~~~~~
Toutes les requêtes vers cette API doivent inclure les paramètres suivants :

- **headers** : dictionnaire contenant les en-têtes HTTP requis
  - `Content-Type`: doit être `application/json`
  - `x-api-key`: clé API pour authentification
- **json** : dictionnaire contenant les données envoyées dans la requête
  - `filename`: nom du fichier à télécharger
  - `user_id`: identifiant de l'utilisateur

.. code-block:: python

    response = requests.post(
        'https://fkaw8ao81j.execute-api.ca-central-1.amazonaws.com/dev/get-upload-url',
        headers={
            'Content-Type': 'application/json',
            'x-api-key': API_KEY
        },
        json={
            'filename': filename,
            'user_id': user_id,
        }
    )

Réponse
~~~~~~~~~~~~~
L'API renvoie un objet JSON contenant l'URL temporaire où le fichier peut être téléchargé.

- `upload_url` (string): L'URL à utiliser pour télécharger votre fichier.    

.. code-block:: python

    if response.status_code == 200:
        data = response.json()
        upload_url = data['upload_url']
    else:
      print({reponse.status_code} : {response.text})   


upload-file
----------------
Cet API vous permet de télécharger un fichier pour lequel vous souhaitez créer une transcription. Il requiert un URL généré 
en utilisant le point de terminaison get-upload-url.

Points de terminaison
~~~~~~~~~~~~~~~~~~~~~~~~~
- **POST URL_DE_TÉLÉCHARMENT**  
       
Paramètres
~~~~~~~~~~~~~
Toutes les requêtes vers cette API doivent inclure les paramètres suivants :

- **headers** : dictionnaire contenant les en-têtes HTTP requis
  - **x-amz-meta-user-id** : L'identifiant de l'utilisateur faisant la requête
  - **x-amz-meta-language** : `fr/en` La langue de l'enregistrement.

Réponse
~~~~~~~~~~~~~
L'API retourne une réponse contenant un code de succès ou d'erreur. 

.. code-block:: python
  
    with open(file_path, 'rb') as f:
        upload_response = requests.put(
            upload_url,
            data=f,
            headers={
                'x-amz-meta-user-id': user_id,
                'x-amz-meta-language': lang
            }
        )

    if upload_response.status_code != 200:
        print(f"Upload failed: {upload_response.status_code} : {upload_response.text}")
   







