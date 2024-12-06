\chapter{Data structures}

In \mmg{}, several data structures are defined in order to represent and manipulate different entities such as tetrahedra, triangles, or meshes.

\section{Mesh}

The main data structure that is used throughout \mmg{} is the mesh structure \texttt{MMG5\_Mesh}.
This structure contains the following fields:

\begin{itemize}
\item \texttt{dim}   : integer, mesh dimension
\item \texttt{memMax}: size t Maximum memory available
\item \texttt{memCur}: size t Current memory used
\item \texttt{gap}   : double Gap for table reallocation
\item \texttt{ver}   : integer Version of the mesh file

\end{itemize}
