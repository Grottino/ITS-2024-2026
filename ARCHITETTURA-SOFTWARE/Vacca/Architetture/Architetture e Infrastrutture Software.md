Un sistema è un insieme di hardware e software che collaborano tra loro

- Architettura software = Sistema operativo dove arrivano molti oggetti software che hanno uno scopo  (ad esempio il PC è un’architettura)
--------------------------------------------------------------------------
componenti pc
parte fondamentale dell'hardware è la cpu central processing unit.
RAM = Random access memory. E' volatile
Storage = memoria di massa (hardisk).
i bass collegano cpu ram schede video.
input output = tastiera mouse
Tra server si collegano vari dispositivi di rete.
Architettura = gestione componenti di un'applicazione come sono organizzati e come si descrivono.
Una buona architettura deve essere: sicura(mantenimento sicuro di dati, non bucabile), affidabile, scalabile(ovvero essere in grado di ridimensionarsi riuscendo a gestire aumento di dati), mantenibile(semplice da aggiornare e semplice da correggere), evitare single point of failure, usare pattern di sviluppo
2 modi per scalare:
- scaling verticale = aggiugi risorse ad un nodo (componente)
- scaling orizzontale = aggiungi nodi

Pattern
monolitico = quando tutte le funzionalità sono contenute in un unico blocco
pro facile da gestire contro con il tempo diventa difficile gestirlo
client-server = un richiedente di funzioni ed un server elabora e risponde (praticamente tutte applicazioni web)
Layered = vari livelli con possibili linguaggi diversi che creano un pattern e parlano con il blocco successivo o quello precedente  
microservizi = quando l'applicazione è divisa in diversi servizi indipendenti e specializzati che comunicano tra loro (es: parte dove ci si registra e si fa il login). Quindi si prende un gruppo di funzionalità e lo si mette in un servizio. Come contro ha la complessità del sistema
eventdriven = pattern di cui i componenti reagiscono ad eventi generati da altri componenti

Un azienda che ha dei server fisici è considerata On-Premise ma con dei costi alti come: Corrente, Raffreddamento (altrimenti ti va a fuoco il server), licenze e manutenzione, pezzi di ricambio in caso di guasto.
On-premise in realtà è quando sei responsabile di un asset non per forza statico ma anche mobile come il telefonino

Virtualizzazione e Containerizzazione

la virtualizzazione è la pratica che permette di eseguire più sistemi operativi (macchine virtuali) su un unico server. Emula hardware con software su cui posso installare un sistema operativo.
Docker(containerizzazione) = consente gestire container che eseguono funzioni e condividono il cuore con la stessa macchina che ospita ma rimanendo isolati 
Container è un oggetto essenziale con libreria essenziale

Infrastrutture Cloud
delle piattaforme virtuali dove depositare dati
piani di pagamento a consumo
qualsiasi cosa è un servizio

vantaggi: scalabilità, pagamento a consumo, tempo di provisioning migliore(quando devo aggiungere una risorsa a qualcosa, fornire risorse)
SAAS
software as a service
Bilanciamento di carico(load balancing)
HA high ability = alta scalabiltà. ho disponibile per il maggior tempo possibile il mio sistema (down time vicino allo 0) utilizzando la ridondanza

modalità HA detta fail over = modalità di passaggio automatico da sistema primario a sistema secondario
load balancing
Sicurezza e monitoraggio 
di sicurezza parleremo di firewall, vpn, sicurezza applicativa

passaggi chiave per gestire un'architettura
comprendere gli obbiettivi(richieste, numeri di dati, costi, livello di servizio, sla)
progettare architettura hardware e software
scegliere l'infrastruttura in base ai costi 
competenze
piani di test
monitoraggio continuo

I server sono fatti per funzionare 24/7

