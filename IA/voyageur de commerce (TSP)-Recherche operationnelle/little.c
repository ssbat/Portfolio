/**
 * Projec : gtsp (voyageur de commerce)
 *
 * Date   : 07/04/2014
 * Author : Olivier Grunder
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define NBR_TOWNS 6

/* Distance matrix */
double dist[NBR_TOWNS][NBR_TOWNS] ;

/* Each edge has a starting and ending node */
int starting_town[NBR_TOWNS] ;
int ending_town[NBR_TOWNS] ;

/* no comment */
int best_solution[NBR_TOWNS] ;
double best_eval=-1.0 ;


/**
 * Berlin52 :
 *  6 towns : Best solution (2315.15): 0 1 2 3 5 4
 * 10 towns : Best solution (2826.50): 0 1 6 2 7 8 9 3 5 4
 */
float coord[NBR_TOWNS][2]=//coord des towns
{
    {565.0,  575.0},
    { 25.0,  185.0},
    {345.0,  750.0},
    {945.0,  685.0},
    {845.0,  655.0},
    {880.0,  660.0}
} ;

void matrice_distance(double dist[NBR_TOWNS][NBR_TOWNS],float coord[NBR_TOWNS][2])
{
    for (int i=0;i<NBR_TOWNS;i++)
    {
        for (int j=0;j<NBR_TOWNS;j++)
        {
            if (i==j){
                dist[i][j]=-1;
            }
            else{
                dist[i][j]=sqrt(pow(coord[j][0]-coord[i][0],2)+pow(coord[j][1]-coord[i][1],2));
            }
        }
    }
}






/**
 * print a matrix
 */
void print_matrix(double d[NBR_TOWNS][NBR_TOWNS])
{
    int i, j ;
    for (i=0; i<NBR_TOWNS; i++)
    {
        printf ("%d:", i) ;
        for (j=0; j<NBR_TOWNS; j++)
        {
            printf ("%6.1f ", d[i][j]) ;
        }
        printf ("\n") ;
    }
}



/**
 * print a solution
 */
void print_solution(int* sol, double eval)
{
    int i ;
    printf ("(%.2f): ", eval) ;
    for (i=0; i<NBR_TOWNS; i++)
        printf ("%d ",sol[i]);
    printf("\n") ;
}




/**
 * evaluation of a solution
 */
double evaluation_solution(int* sol)//distance totale
{
    double eval=0 ;
    int i ;
    for (i=0; i<NBR_TOWNS-1; i++)
    {
        eval += dist[sol[i]][sol[i+1]] ;
    }
    eval += dist[sol[NBR_TOWNS-1]][sol[0]] ;

    return eval ;

}



int InList(int*liste,int length,int elt){
    int trouver=0;
    for (int i=0;i<length;i++){
        if(liste[i]==elt){
            trouver=1;
        }
    }
    return trouver;
}

/**
 * nearest neighbour solution
 */
double build_nearest_neighbour()
{
    /* solution of the nearest neighbour */
    int i, sol[NBR_TOWNS] ;

    /* evaluation of the solution */
    double eval = 0 ;

    sol[0] = 0 ;
    int open_list[]={-1,-1,-1,-1,-1,0};

    for (int j=0;j<NBR_TOWNS-1;j++)
    {
        int city=sol[j];   
        double min=INFINITY;
        int indice_min=-1;

        for (int k=0;k<NBR_TOWNS;k++)
        {
            if(dist[city][k]<=min && k!=city && !InList(open_list,6,k)){
                min=dist[city][k];
                // printf("%f\n",min);
                indice_min=k;
                
            }   
        }
            open_list[j]=indice_min;
            sol[j+1]=indice_min;
    };

      eval = evaluation_solution(sol) ;
      printf("Nearest neighbour ") ;
      print_solution (sol, eval) ;
     
      for (i=0;i<NBR_TOWNS;i++) best_solution[i] = sol[i] ;
      best_eval  = eval ;
    return eval ;
}




/**
 *  Build final solution
 */
void build_solution()
{
    int i, solution[NBR_TOWNS] ;

    int indiceCour = 0;
    int villeCour = 0;

    while (indiceCour < NBR_TOWNS)
    {

        solution[indiceCour] = villeCour ;

        // Test si le cycle est hamiltonien
        for (i = 0; i < indiceCour; i++)
        {
            if (solution[i] == villeCour)
            {
                /* printf ("cycle non hamiltonien\n") ; */
                return;
            }
        }
        // Recherche de la ville suivante
        int trouve = 0;
        int i = 0;
        while ((!trouve) && (i < NBR_TOWNS))
        {
            if (starting_town[i] == villeCour)
            {
                trouve = 1;
                villeCour = ending_town[i];
            }
            i++;
        }
        indiceCour++;
    }

    double eval = evaluation_solution(solution) ;

    if (best_eval<0 || eval < best_eval)
    {
        best_eval = eval ;
        for (i=0; i<NBR_TOWNS; i++)
            best_solution[i] = solution[i] ;
        printf ("New best solution: ") ;
        print_solution (solution, best_eval) ;
    }
    return;
}

double minimumOfColumn(double M[NBR_TOWNS][NBR_TOWNS],int j){
    double min=INFINITY;
    // printf("!!!!!!!!%f\n",M[0][j]);

    for (int i=0;i<NBR_TOWNS;i++){
        if(M[i][j]<=min && i!=j && M[i][j]>=0){
            min=M[i][j];
        }
        // printf("$$%f\n",min);
    }
    return min;
}


double minimumOfRow(double liste[NBR_TOWNS]){
    double min=INFINITY;
    for(int i=0;i<NBR_TOWNS;i++){
        if(liste[i]<min && liste[i]>=0 && liste[i]>=0){
            min=liste[i];
        }
    }
    return min;
}
double soustraction_ligne(double d0[NBR_TOWNS][NBR_TOWNS],int ligne,double min_row)
{
    for (int j=0; j<NBR_TOWNS; j++){
                if(ligne!=j && d0[ligne][j]>=0)d0[ligne][j]-=min_row;
            }
            // printf ("\n") ; 
}
double soustraction_colonne(double d0[NBR_TOWNS][NBR_TOWNS],int colonne,double min_col)
{
    for(int ligne=0;ligne<NBR_TOWNS;ligne++){
            if(ligne!=colonne && d0[ligne][colonne]>=0)d0[ligne][colonne]-=min_col;
        }
}
/**
 *  Little Algorithm
 */
void little_algorithm(double d0[NBR_TOWNS][NBR_TOWNS], int iteration, double eval_node_parent)
{
    if (iteration == NBR_TOWNS)
    {
        build_solution ();
        return;
    }
    print_matrix(d0);
    printf("\n");
    /* Do the modification on a copy of the distance matrix */
    double d[NBR_TOWNS][NBR_TOWNS] ;
    memcpy (d, d0, NBR_TOWNS*NBR_TOWNS*sizeof(double)) ;
    // int i, j ;
    double eval_node_child = eval_node_parent;



/**
     * substract the min of the rows and the min of the columns
     * and update the evaluation of the current node
     *  TO COMPLETE
     *  ...
     *  ...
     */
    int i, j ;//soustraction des rows
    for (int ligne=0; ligne<NBR_TOWNS; ligne++){
                // printf ("%d:", i) ;

        double min_row=minimumOfRow(d[ligne]);
        if(min_row!=INFINITY)eval_node_child+=min_row;
        soustraction_ligne(d,ligne,min_row);

    }
    // print_matrix(d);
    //soustraction des colonnes
    for (int colonne=0; colonne<NBR_TOWNS; colonne++){
                double min_col=minimumOfColumn(d,colonne);
                
                if(min_col!=INFINITY)eval_node_child+=min_col;
                // printf("%f\t",min_col); // printf("\n");
                soustraction_colonne(d,colonne,min_col);
        }


    

    /* Cut : stop the exploration of this node */
    if (best_eval>=0 && eval_node_child >= best_eval)
        return;


    /**
     *  Compute the penalities to identify the zero with max penalty
     *  If no zero in the matrix, then return, solution infeasible
     *  TO COMPLETE
     *  ...
     *  ...
     */
    /* row and column of the zero with the max penalty */
    // int izero=-1, jzero=-1 ;


    int izero=-1, jzero=-1 ;
    double penalty_max=0;
    for (int ligne=0; ligne<NBR_TOWNS; ligne++){
        for (int colonne=0; colonne<NBR_TOWNS; colonne++){
            if(d[ligne][colonne]==0){//j'ai trouvé un zero
                double min_ligne_zero=INFINITY;
                double min_col_zero=INFINITY;
                // double min_ligne_zero_indice=
                // printf("!");
                for (int col2=0; col2<NBR_TOWNS; col2++){//parcours 3al ligne
                    if(col2!=colonne && d[ligne][col2]<min_ligne_zero && ligne!=col2 && d[ligne][col2]>=0){// printf("@");    
                        min_ligne_zero=d[ligne][col2];
                    }
                }
                for (int ligne2=0; ligne2<NBR_TOWNS; ligne2++ ){//parcours 3al ligne
                    if(ligne2!=ligne && d[ligne2][colonne]<min_col_zero && ligne2!=colonne && d[ligne2][colonne]>=0){min_col_zero=d[ligne2][colonne];}
                }
                // printf("min_ligne_zero:%f \n",min_ligne_zero);printf("min_col_zero:%f \n",min_col_zero);
                if(penalty_max<min_col_zero+min_ligne_zero)
                {
                    penalty_max=min_col_zero+min_ligne_zero;
                    izero=ligne;jzero=colonne;
                }
            }
        }
    
    }
    if (izero == -1 || jzero == -1)
    {
        return;
    }
    starting_town[iteration]=izero;
    ending_town[iteration]=jzero;
    printf("(%i,%i)->%f",izero,jzero,penalty_max);
    /**
     *  Store the row and column of the zero with max penalty in
     *  starting_town and ending_town
     *  TO COMPLETE
     *  ...
     *  ...
     */

    /* Do the modification on a copy of the distance matrix */
    double d2[NBR_TOWNS][NBR_TOWNS] ;
    memcpy (d2, d, NBR_TOWNS*NBR_TOWNS*sizeof(double)) ;


    for (int colonne=0;colonne<NBR_TOWNS;colonne++){
            d2[izero][colonne]=-1;
    }
    for (int ligne=0;ligne<NBR_TOWNS;ligne++){
            d2[ligne][jzero]=-1;
    }
    /**
     *  Modify the matrix d2 according to the choice of the zero with the max penalty
     *  TO COMPLETE
     *  ...
     *  ...
     */

    /* Explore left child node according to given choice */
    little_algorithm(d2, iteration + 1, eval_node_child);

    /* Do the modification on a copy of the distance matrix */
    memcpy (d2, d, NBR_TOWNS*NBR_TOWNS*sizeof(double)) ;
    d2[izero][jzero]=-1;
    /**
     *  Modify the dist matrix to explore the other possibility : the non-choice
     *  of the zero with the max penalty
     *  TO COMPLETE
     *  ...
     *  ...
     */

    /* Explore right child node according to non-choice */
    little_algorithm(d2, iteration, eval_node_child);

}




/**
 *
 */
int main (int argc, char* argv[])
{

    best_eval = -1 ;

    /* Print problem informations */
    printf ("Points coordinates:\n") ;
    int i ;
    for (i=0; i<NBR_TOWNS; i++)
    {
        printf ("Node %d: x=%f, y=%f\n", i, coord[i][0], coord[i][1]) ;
    }
    printf ("\n") ;


    /* Calcul de la matrice des distances */
    /**
     *  TO COMPLETE
     *  ...
     *  ...
     */

    // printf ("Distance Matrix:\n") ;
    matrice_distance(dist,coord);
    // print_matrix (dist);
   
    // build_nearest_neighbour();

    // double liste[]={34,324,5,23,2324,145,789};
    // printf("%f\n",minimumOfRow(liste));
    
    /** Nearest Neighbour heuristic : uncomment when needed
     *
     *  double nearest_neighbour = build_nearest_neighbour() ;
     */

    //  Little : uncomment when needed
    
    int iteration = 0 ;
    double lowerbound = 0.0 ;
    
    little_algorithm(dist, iteration, lowerbound) ;

    printf("Best solution:") ;
    print_solution (best_solution, best_eval) ;
    

    printf ("Hit RETURN!\n") ;
    getchar() ;

    return 0 ;
    // for (int ligne=0; ligne<NBR_TOWNS; ligne++){
    //             // printf ("%d:", i) ;

    //     double min_row=minimumOfRow(dist[ligne]);
    //     // eval_node_child+=min_row;
    //     soustraction_ligne(dist,ligne,min_row);

    // }
    // print_matrix(dist);
    // printf("\n");
    // //soustraction des colonnes
    // for (int colonne=0; colonne<NBR_TOWNS; colonne++){
    //             double min_col=minimumOfColumn(dist,colonne);
    //             // eval_node_child+=min_col;
    //             // printf("%f\t",min_col); // printf("\n");
    //             soustraction_colonne(dist,colonne,min_col);
    //     }
    // print_matrix(dist);

    // int izero=-1, jzero=-1 ;
    // double penalty_max=0;
    // for (int ligne=0; ligne<NBR_TOWNS; ligne++){
        
    //     for (int colonne=0; colonne<NBR_TOWNS; colonne++){
    //         if(dist[ligne][colonne]==0){//j'ai trouvé un zero
    //             double min_ligne_zero=9999999;
    //             double min_col_zero=9999999;
    //             // double min_ligne_zero_indice=
    //             printf("!");
    //             for (int col2=0; col2<NBR_TOWNS; col2++){//parcours 3al ligne
    //                 if(col2!=colonne && dist[ligne][col2]<min_ligne_zero && ligne!=col2 && dist[ligne][col2]>=0){
    //                     printf("@");    
    //                     min_ligne_zero=dist[ligne][col2];
    //                 }
    //             }
    //             for (int ligne2=0; ligne2<NBR_TOWNS; ligne2++ ){//parcours 3al ligne
    //                 if(ligne2!=ligne && dist[ligne2][colonne]<min_col_zero && ligne2!=colonne && dist[ligne2][colonne]>=0){min_col_zero=dist[ligne2][colonne];}

    //             }
    //             printf("min_ligne_zero:%f \n",min_ligne_zero);
    //             printf("min_col_zero:%f \n",min_col_zero);

    //             if(penalty_max<min_col_zero+min_ligne_zero)
    //             {
    //                 penalty_max=min_col_zero+min_ligne_zero;
    //                 izero=ligne;
    //                 jzero=colonne;

    //             }
                
    //         }
    //     }
    
    // }
    // printf("(%i,%i)->%f",izero,jzero,penalty_max);
}

// resultat à la fin 2315

// 0-1-3-5-4


